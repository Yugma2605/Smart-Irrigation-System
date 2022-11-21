import keras
from keras.models import Model
from keras.layers import Dense
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

#trdata = ImageDataGenerator(rescale=1. / 255,
					 #  rotation_range=20,
					  # width_shift_range=0.2,
					   #height_shift_range=0.2,
					   #horizontal_flip=True,
					   #fill_mode='nearest')
                                     
trdata = ImageDataGenerator()
traindata = trdata.flow_from_directory(directory="Output/train",target_size=(224,224))
tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory="Output/val", target_size=(224,224))

from keras.applications.vgg19 import VGG19
vggmodel = VGG19(weights='imagenet', include_top=True)

vggmodel.summary()

for layers in (vggmodel.layers)[:19]:
    print(layers)
    layers.trainable = False
    
X= vggmodel.layers[-2].output
predictions = Dense(2, activation="softmax")(X)
model_final = Model(input = vggmodel.input, output = predictions)

model_final.compile(loss = "categorical_crossentropy", optimizer = optimizers.SGD(lr=0.0001, momentum=0.9), metrics=["accuracy"])

model_final.summary()

from keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint = ModelCheckpoint("vgg16_NP.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
early = EarlyStopping(monitor='val_accuracy', min_delta=0, patience=40, verbose=1, mode='auto')
hist = model_final.fit_generator(generator= traindata, steps_per_epoch= 20, epochs= 100, validation_data= testdata, validation_steps=10, callbacks=[checkpoint,early])
model_final.save_weights("vgg16_NP.h5")

print(hist.history)
field_names= list( hist.history.keys())
print(field_names)
import csv

with open('tfNP.csv', 'w') as f:
    for key in hist.history.keys():        
        f.write("%s,%s\n"%(key,hist.history[key]))

