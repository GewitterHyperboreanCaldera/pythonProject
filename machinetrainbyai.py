from tensorflow.keras.datasets import mnist
import tensorflow as tf
import math

# Redefining NaiveDense, NaiveSequential, BatchGenerator, one_training_step, update_weights (if needed)
# to ensure the context is self-contained for the fix within this cell.
# Ideally, these would be in their own cells and not repeated here.

# --- Start of necessary context from previous cells ---
class NaiveDense:
  def __init__ (self, input_size, output_size, activation):
    self.activation = activation
    w_shape = (input_size,output_size)
    w_initial_value = tf.random.uniform(w_shape, minval=0, maxval=1e-1)
    self.W = tf.Variable(w_initial_value)

    b_shape = (output_size,)
    b_initial_value = tf.zeros(b_shape)
    self.b = tf.Variable(b_initial_value)

  def __call__(self, inputs):
    return self.activation(tf.matmul(inputs, self.W) + self.b)

  @property
  def weights(self):
    return [self.W, self.b]

class NaiveSequential:
  def __init__(self, layers):
    self.layers = layers

  def __call__(self, inputs):
    x = inputs
    for layer in self.layers:
      x = layer(x)
    return x

  @property
  def weights(self):
    weights = []
    for layer in self.layers:
      weights += layer.weights
    return weights

class BatchGenerator:
  def __init__(self, images, labels, batch_size=128):
    assert len(images) == len(labels)
    self.index = 0
    self.images = images
    self.labels = labels
    self.batch_size = batch_size
    self.num_batches = math.ceil(len(images) / batch_size)

  def next(self):
    # Ensure index wraps around if called multiple times beyond data size (for multiple epochs)
    # Or, reset index for each epoch in fit function (better approach for multiple epochs)
    if self.index >= len(self.images):
        self.index = 0 # Reset for next epoch if not handled externally

    start_idx = self.index
    end_idx = self.index + self.batch_size
    images = self.images[start_idx : end_idx]
    labels = self.labels[start_idx : end_idx]
    self.index = end_idx
    return images, labels

from tensorflow.keras import optimizers
optimizer = optimizers.SGD(learning_rate = 1e-3)

def update_weights(gradients, weights):
  optimizer.apply_gradients(zip(gradients, weights))

def one_training_step(model, images_batch, labels_batch):
  with tf.GradientTape() as tape:
    predictions = model(images_batch)
    per_sample_losses = tf.keras.losses.sparse_categorical_crossentropy(
        labels_batch, predictions
    )
    average_loss = tf.reduce_mean(per_sample_losses)
  gradients = tape.gradient(average_loss, model.weights)
  update_weights(gradients, model.weights)
  return average_loss
# --- End of necessary context from previous cells ---


def fit(model, images, labels, epochs, batch_size = 128):
  for epoch_counter in range(epochs):
    print(f"Epoch {epoch_counter}")
    data_generator = BatchGenerator(images, labels, batch_size) # Instantiate BatchGenerator
    for batch_counter in range(data_generator.num_batches): # Use a different variable name
      images_batch, labels_batch = data_generator.next() # Call .next() on the BatchGenerator instance
      loss =  one_training_step(model, images_batch, labels_batch)
      if batch_counter % 100 == 0:
        print(f"loss at batch {batch_counter}: {loss: .2f}")

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255
test_images = test_images.reshape((10000 , 28 * 28))
test_images = test_images.astype("float32") / 255

# Re-create the model as it was defined in a prior cell (if not already in scope)
model = NaiveSequential([
    NaiveDense(input_size=28 * 28, output_size=512, activation=tf.nn.relu),
    NaiveDense(input_size=512, output_size=10, activation=tf.nn.softmax)
])

fit(model, train_images, train_labels, epochs=10, batch_size=128)