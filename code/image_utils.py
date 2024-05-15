

def save_image(image_url, save_directory, filename=None):
    """
    Download an image from a URL and save it to the specified directory.

    Parameters:
        image_url (str): The URL of the image to download.
        save_directory (str): The directory where the image will be saved.
        filename (str, optional): The filename to use for the saved image. 
            If not provided, the filename will be derived from the URL.

    Returns:
        str: The path to the saved image.

    """
    import os
    import requests
    # Send a GET request to the URL
    response = requests.get(image_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the content of the response (the image data)
        image_data = response.content
        
        # If filename is not provided, derive it from the URL
        if not filename:
            filename = os.path.basename(image_url)
        
        
        # Write the image data to a file in the specified directory
        image_path = os.path.join(save_directory, filename)
        with open(image_path, 'wb') as f:
            f.write(image_data)
        
        return image_path
    else:
        print('Failed to download image from', image_url)
        return None

