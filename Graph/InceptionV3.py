acc = [0.4414893686771393, 0.478723406791687, 0.49468085169792175, 0.5053191781044006, 0.5053191781044006, 0.5478723645210266, 0.5478723645210266, 0.6276595592498779, 0.5904255509376526, 0.5531914830207825, 0.7180851101875305, 0.8723404407501221, 0.8510638475418091, 0.8989361524581909, 0.9095744490623474, 0.9521276354789734, 0.957446813583374, 0.9840425252914429, 0.9521276354789734, 0.9734042286872864, 0.9680851101875305, 0.9627659320831299, 0.9840425252914429, 0.9840425252914429, 0.9893617033958435, 0.978723406791687, 0.9840425252914429, 1.0, 0.9840425252914429, 1.0, 1.0]

val_acc = [0.6129032373428345, 0.6451612710952759, 0.4838709533214569, 0.5806451439857483, 0.5483871102333069, 0.6451612710952759, 0.5483871102333069, 0.6129032373428345, 0.6451612710952759, 0.7419354915618896, 0.8064516186714172, 0.9032257795333862, 0.9032257795333862, 0.9032257795333862, 0.8387096524238586, 0.9032257795333862, 0.9677419066429138, 0.9354838728904724, 0.9032257795333862, 0.9032257795333862, 0.9677419066429138, 0.9677419066429138, 0.9354838728904724, 0.9677419066429138, 0.9677419066429138, 0.9354838728904724, 0.9354838728904724, 0.8709677457809448, 1.0, 0.9677419066429138, 0.9677419066429138]

loss = [0.7495517134666443, 0.7544447779655457, 0.6956872940063477, 0.6819202303886414, 0.6937363147735596, 0.6567111015319824, 0.664385974407196, 0.6294711828231812, 0.6317805647850037, 0.6188370585441589, 0.5320388078689575, 0.381338894367218, 0.343014657497406, 0.25694337487220764, 0.22880832850933075, 0.16991464793682098, 0.16870300471782684, 0.10791073739528656, 0.11921010166406631, 0.09254389256238937, 0.08939018845558167, 0.09405087679624557, 0.05616074800491333, 0.055500101298093796, 0.053724613040685654, 0.045639798045158386, 0.04357843101024628, 0.023283664137125015, 0.04299582913517952, 0.020027944818139076, 0.014762356877326965]

val_loss = [0.6455829739570618, 0.6867740750312805, 0.6496912837028503, 0.6730104684829712, 0.6827635765075684, 0.6137527227401733, 0.5843085646629333, 0.5926328301429749, 0.6034553050994873, 0.5877680778503418, 0.4384694993495941, 0.38579750061035156, 0.29050999879837036, 0.29904019832611084, 0.23868370056152344, 0.2713433504104614, 0.22006236016750336, 0.23128153383731842, 0.1624898612499237, 0.2016129344701767, 0.13143369555473328, 0.13049684464931488, 0.1733769029378891, 0.18435844779014587, 0.11038800328969955, 0.22578728199005127, 0.1883959323167801, 0.1262429654598236, 0.06496208161115646, 0.2745681703090668, 0.12648655474185944]

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