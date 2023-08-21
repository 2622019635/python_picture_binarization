from PIL import Image
from pathlib import Path


class PictureBinarization:
    def __init__(self, path='./', threshold=180, is_overly=False, output_path_prefix='binarization_'):
        self.path = path
        self.threshold = threshold
        self.is_overly = is_overly
        self.output_path_prefix = output_path_prefix

        self.on_start_binarizing = None
        self.on_finish_binarizing = None

        # check input
        if not isinstance(self.path.strip(), str) or not isinstance(self.output_path_prefix.strip(), str):
            print("Input and output paths must be strings")
            exit(1)
        if not isinstance(self.threshold, int) or self.threshold < 0 or self.threshold > 255:
            print("Threshold must be an integer between 0 and 255")
            exit(1)

    
    def create_binarized_picture(self, path, threshold, output_path):
        if self.on_start_binarizing:
            self.on_start_binarizing(path, threshold, output_path)

        try:
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
            picture = img.point(table, '1')
            
            # save image
            picture.save(output_path)
            if self.on_finish_binarizing:
                self.on_finish_binarizing(path, threshold, output_path)
        except Exception as e:
            print("Error:", e)
    
    # picture binarization
    def picture_binarization(self):
        path = Path(self.path)
        if path.is_file():
            if not self.is_overly:
                output_path = path.parent.joinpath(self.output_path_prefix + path.name)
                self.create_binarized_picture(self.path, self.threshold, output_path)
            else:
                self.create_binarized_picture(self.path, self.threshold, self.path)
        else:
            for file in path.iterdir():
                if file.is_file():
                    file_path = file.parent.joinpath(file.name)
                    if not self.is_overly:
                        output_path = file.parent.joinpath(self.output_path_prefix + file.name)
                        self.create_binarized_picture(str(file_path), self.threshold, str(output_path))
                    else:
                        self.create_binarized_picture(str(file_path), self.threshold, str(file_path))


    def set_on_start_binarizing(self, func):
        self.on_start_binarizing = func
    
    def set_on_finish_binarizing(self, func):
        self.on_finish_binarizing = func



if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser(description='picture binarization')
    parse.add_argument('-p', '--path', type=str, metavar='\b', help='Picture path.')
    parse.add_argument('-t', '--threshold', type=int, default=180, metavar='\b', choices=tuple(range(256)), help='Boundary values for black and white. [0-255]')
    parse.add_argument('-o', '--overly', type=bool, default=False, metavar='\b', help='Is file overly.')
    parse.add_argument('--prefix', type=str, default='binarization_', metavar='\b', help='Output file prefix. [default: binarization_]')
    args = parse.parse_args()
    if args.path == '.':
        args.path = './'
    
    def on_start_binarizing(path, threshold, output_path):
        print('Start binarizing:', path)
        print('Threshold:', threshold)
        print('Output path:', output_path)

    pct = PictureBinarization(args.path, args.threshold, args.overly, args.prefix)
    pct.set_on_start_binarizing(on_start_binarizing)
    pct.picture_binarization()
