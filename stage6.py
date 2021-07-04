#new function to create a jpg from a byte array
def savejpg(a, filename, fmt='jpeg'):
    a = np.uint8(np.clip(a, 0, 255))
    f = BytesIO()
    PIL.Image.fromarray(a).save(filename, fmt)

# the code will start here on stage 6
# we need some file handling    
import os, re, os.path
# create the outputs folder if it does not exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

#clean up any existing output files
for root, dirs, files in os.walk("outputs"):
    for file in files:
        os.remove(os.path.join(root, file))


layer = "mixed4d_3x3_bottleneck_pre_relu"  #@param ["mixed4d_3x3_bottleneck_pre_relu", "mixed3a", "mixed3b", "mixed4a", "mixed4c", "mixed5a"]
iter_n = 5 #@param {type:"slider", max: 50}
strength = 150 #@param {type:"slider", max: 1000}
zooming_steps = 3 #@param {type:"slider", max: 512}
zoom_factor = 1.1 #@param {type:"number"}

frame = img0
img_y, img_x, _ = img0.shape
for i in range(zooming_steps):
  frame = render_deepdream(tf.square(T(layer)), frame, False)
  clear_output()
  filename="outputs/dreamstage" + str(i) +".jpg"
  showarray(frame)
  #save each iteration in the outputs folder
  savejpg(frame, filename)
  newsize = np.int32(np.float32(frame.shape[:2])*zoom_factor)
  frame = resize(frame, newsize)
  frame = frame[(newsize[0]-img_y)//2:(newsize[0]-img_y)//2+img_y,
                (newsize[1]-img_x)//2:(newsize[1]-img_x)//2+img_x,:]
  
