import cv2
import numpy as np
import mediapipe as mp

def remove_background(image_path, background_color=(255, 255, 255)):
    """
    Removes the background from an image using Mediapipe Selfie Segmentation.

    Args:
        image_path (str): Path to the input image.
        background_color (tuple): RGB tuple for the background color.

    Returns:
        np.ndarray: Image with the background removed or replaced.
    """
    # Initialize Mediapipe Selfie Segmentation
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

    # Read the input image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform segmentation
    results = segmentation.process(image_rgb)

    # Create a mask where background is black and foreground is white
    mask = results.segmentation_mask > 0.5
    mask = mask.astype(np.uint8)

    # Create a blank background with the specified color
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = background_color

    # Combine the original image with the background
    foreground = cv2.bitwise_and(image, image, mask=mask)
    inverse_mask = cv2.bitwise_not(mask * 255)
    background = cv2.bitwise_and(bg_image, bg_image, mask=inverse_mask)
    final_image = cv2.add(foreground, background)

    return final_image

# Example usage
if __name__ == "__main__":
    input_image_path = "D:\personal\Profile_Talha.jfif"  # Replace with your image path
    output_image_path = "output.jpg"

    result_image = remove_background(input_image_path, background_color=(255, 255, 255))
    cv2.imwrite(output_image_path, result_image)
    print(f"Background removed image saved at {output_image_path}")
