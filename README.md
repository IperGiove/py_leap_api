# TryLeap Python API
The py_leap_api Python package provides a simple interface for interacting with the TryLeap service, a cloud-based platform for generating images using artificial intelligence.

## Installation
You can install the py_leap_api package using pip:

```bash
pip install py_leap_api
```

## Getting Started
First, you'll need to create an account on the TryLeap website and obtain an API key.

Once you have an API key, you can use the TryLeap class to interact with the service. Here's a simple example that creates a model, uploads some images, and generates some images based on a prompt:

```python
from tryleap import TryLeap

# Create a TryLeap object with your API key
api_key = "your-api-key"
await leap = TryLeap(api=api_key)

# Create a model
model = await leap.create_model("My Model")

# Overwrite the TryLeap object with the new model id
await leap = TryLeap(api=api_key, model=model)

# Upload some images
urls = [
    "https://example.com/image1.png",
    "https://example.com/image2.png",
    "https://example.com/image3.png",
]
await leap.upload_images_url(urls)

# Train the model
await leap.training_model()
```

Ideally if you have a webhook url you can provide it to training_model in order to know when the training finished.
Otherwise you can fetch the status that return from the function.

```python
# Generate some images
prompt = "a cat sitting on a couch"
images = await leap.generate_image(prompt, number_images=3)

# Retrieve the output images
output_images = await leap.output_images()
```

# License
This library is licensed under the MIT License. See the LICENSE file for details.
