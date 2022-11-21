acc = [0.4308510720729828, 0.457446813583374, 0.46276596188545227, 0.5, 0.5159574747085571, 0.5053191781044006, 0.5372340679168701, 0.5531914830207825, 0.542553186416626, 0.6063829660415649, 0.6489361524581909, 0.8191489577293396, 0.8936170339584351, 0.9468085169792175, 0.9521276354789734, 0.9521276354789734, 0.9627659320831299, 0.9946808218955994, 0.978723406791687, 0.978723406791687, 0.9840425252914429, 0.9840425252914429, 0.9946808218955994, 0.9840425252914429, 1.0, 0.9840425252914429, 0.9946808218955994, 1.0, 1.0, 1.0, 1.0]
val_acc = [0.4516128897666931, 0.4516128897666931, 0.4193548262119293, 0.4516128897666931, 0.45483869910240173, 0.5161290168762207, 0.5806451439857483, 0.5806451439857483, 0.5806451439857483, 0.6451612710952759, 0.8064516186714172, 0.8064516186714172, 0.9354838728904724, 0.9354838728904724, 0.9032257795333862, 0.9354838728904724, 0.9032257795333862, 0.8709677457809448, 0.9032257795333862, 0.9032257795333862, 0.9677419066429138, 0.9677419066429138, 0.9354838728904724, 0.9354838728904724, 0.9354838728904724, 0.9677419066429138, 1.0, 1.0, 0.9677419066429138, 1.0, 0.9354838728904724]
loss = [0.9278895854949951, 0.8985964059829712, 0.8742126822471619, 0.8023576736450195, 0.8032529354095459, 0.7993612289428711, 0.7504667043685913, 0.6979605555534363, 0.6979778409004211, 0.6508027911186218, 0.5545769929885864, 0.36330556869506836, 0.26548898220062256, 0.15874995291233063, 0.14112631976604462, 0.10415568202733994, 0.11068176478147507, 0.04015231505036354, 0.06577666848897934, 0.046151190996170044, 0.03839986398816109, 0.044425155967473984, 0.048100944608449936, 0.020374342799186707, 0.008038213476538658, 0.06179666891694069, 0.010644313879311085, 0.007708519697189331, 0.010581010952591896, 0.008556432090699673, 0.002237513894215226]
val_loss = [0.9014023542404175, 0.7927238345146179, 0.8168033361434937, 0.8095565438270569, 0.8267444372177124, 0.7423442602157593, 0.6506603956222534, 0.6665273308753967, 0.7008749842643738, 0.5930525064468384, 0.3982986807823181, 0.36322861909866333, 0.19928525388240814, 0.14917193353176117, 0.16902361810207367, 0.1506502777338028, 0.16422675549983978, 0.20121268928050995, 0.17238852381706238, 0.1440940499305725, 0.05876706913113594, 0.07871308922767639, 0.11881571263074875, 0.125418820977211, 0.11379047483205795, 0.04908137395977974, 0.055473119020462036, 0.04758882522583008, 0.08849930018186569, 0.019138028845191002, 0.08324456214904785]
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