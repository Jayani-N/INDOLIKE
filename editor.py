  from PIL import Image, ImageFilter
  
  def image_editor():
      print("Image Editor")
      print("1. Convert to Grayscale")
      print("2. Apply Blur Effect")
      print("3. Resize Image")
  
      choice = input("Enter your choice: ")
      image_path = input("Enter the image file path: ")
  
      try:
          img = Image.open(image_path)
          if choice == '1':
              img = img.convert("L")
              img.show()
              img.save("grayscale_image.jpg")
              print("Grayscale image saved as grayscale_image.jpg")
          elif choice == '2':
              img = img.filter(ImageFilter.BLUR)
              img.show()
              img.save("blurred_image.jpg")
              print("Blurred image saved as blurred_image.jpg")
          elif choice == '3':
              width = int(input("Enter new width: "))
              height = int(input("Enter new height: "))
              img = img.resize((width, height))
              img.show()
              img.save("resized_image.jpg")
              print("Resized image saved as resized_image.jpg")
          else:
              print("Invalid choice!")
      except Exception as e:
          print(f"Error: {e}")
  
  image_editor()
