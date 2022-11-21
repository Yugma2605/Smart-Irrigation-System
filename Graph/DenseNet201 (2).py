acc = [0.49468085169792175, 0.5478723645210266, 0.5585106611251831, 0.563829779624939, 0.6276595592498779, 0.585106372833252, 0.6010638475418091, 0.5904255509376526, 0.6223404407501221, 0.5797872543334961, 0.6808510422706604, 0.728723406791687, 0.7978723645210266, 0.8670212626457214, 0.9042553305625916, 0.9414893388748169, 0.914893627166748, 0.9521276354789734, 0.9414893388748169, 0.9468085169792175, 0.9627659320831299, 0.978723406791687, 0.9734042286872864, 0.9840425252914429, 0.9840425252914429, 0.9893617033958435, 0.9946808218955994, 1.0, 0.978723406791687, 0.9946808218955994, 0.978723406791687]

val_acc = [0.4516128897666931, 0.5161290168762207, 0.5161290168762207, 0.6129032373428345, 0.5161290168762207, 0.6129032373428345, 0.5806451439857483, 0.5161290168762207, 0.6129032373428345, 0.6129032373428345, 0.7419354915618896, 0.8064516186714172, 0.9354838728904724, 0.9032257795333862, 0.9677419066429138, 0.9354838728904724, 0.9354838728904724, 0.8709677457809448, 1.0, 0.9677419066429138, 1.0, 0.9677419066429138, 0.9677419066429138, 0.9677419066429138, 1.0, 1.0, 0.9677419066429138, 0.9677419066429138, 0.9677419066429138, 1.0, 0.9677419066429138]

loss = [0.8694807291030884, 0.7486982345581055, 0.7080346941947937, 0.706643283367157, 0.6215832233428955, 0.6434600353240967, 0.66867595911026, 0.6250412464141846, 0.6058573722839355, 0.6509053707122803, 0.5497808456420898, 0.4429468512535095, 0.35430601239204407, 0.27589496970176697, 0.24960125982761383, 0.176344633102417, 0.2054443508386612, 0.14836980402469635, 0.15416781604290009, 0.1187991201877594, 0.10695244371891022, 0.10231944173574448, 0.09168937057256699, 0.07735900580883026, 0.06216065585613251, 0.08178133517503738, 0.037697527557611465, 0.03612104430794716, 0.045683033764362335, 0.028328433632850647, 0.06263114511966705]

val_loss = [0.7647314667701721, 0.8080523014068604, 0.6941653490066528, 0.612662672996521, 0.700983464717865, 0.6464359164237976, 0.7134043574333191, 0.6690516471862793, 0.6440691947937012, 0.6100571155548096, 0.4796314835548401, 0.4211975336074829, 0.3359014391899109, 0.32451140880584717, 0.2009183168411255, 0.2198973298072815, 0.20258761942386627, 0.16577650606632233, 0.11644583940505981, 0.12263259291648865, 0.09394335001707077, 0.13130086660385132, 0.1224503293633461, 0.09015753865242004, 0.061297252774238586, 0.054214246571063995, 0.10496727377176285, 0.09502243250608444, 0.05799935758113861, 0.053723953664302826, 0.08994194865226746]


import matplotlib.pyplot as plt
initial_epochs = 10
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.ylim([0.2, 1.1])
plt.plot([initial_epochs-1,initial_epochs-1],
          plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.ylim([-0.1, 1.0])
plt.plot([initial_epochs-1,initial_epochs-1],
         plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()