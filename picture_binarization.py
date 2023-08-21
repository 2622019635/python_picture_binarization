from PIL import Image



def picture_binarization(path, threshold, output_path):
    try:
        # check input
        if not isinstance(path, str) or not isinstance(output_path, str):
            raise ValueError("Input and output paths must be strings")
        
        if not isinstance(threshold, int) or threshold < 0 or threshold > 255:
            raise ValueError("Threshold must be an integer between 0 and 255")
        
        # open image
        img = Image.open(path)
        
        # convert to grayscale
        img = img.convert('L')
        
        # create binarization table
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        
        # picture binarization
        photo = img.point(table, '1')
        
        # save image
        photo.save(output_path)
    
    except Exception as e:
        print("Error:", e)
    

if __name__ == '__main__':
		import argparse
		parse = argparse.ArgumentParser(description='picture binarization')
		parse.add_argument('-p', '--path', type=str, metavar='\b', help='Picture path.')
		parse.add_argument('-t', '--threshold', type=int, default=200,metavar='\b', choices=tuple(range(256)), help='Boundary values for black and white. [0-255]')
		parse.add_argument('-o', '--output_path', type=str, metavar='\b', help='Output path.')
		args = parse.parse_args()
		picture_binarization(args.path, args.threshold, args.output_path)