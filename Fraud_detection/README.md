# Fraud Detection

PKU Youth Study center is the supervisor of BDWM BBS. They constantly excert bureaucratic control over the freedom of speech in the BBS. Recently, they are trying to penetrate the self-governing management team, and they raised tremendous objections among the users.

One of their attemptions is, asking their student assistants to apply for the management postitions (Borad Managers, BM). Once they were elected, they would acquire much higher privileges which breaks the delicate balance between the external controler and the users.

In order to carry out their vicious deception, they had to promote among their staff members. Promoting for the voting is specificially prohibited by the rules of the BBS.

To demonstrate the influence of the promotion, the voting behaviors corresponding to the deceptive applicant (`yafeng`), and the valid BM (`naiiive`) were compared.

The duration of the voting is around 7 days, and if there is no influence from the electoral promotion, the time series of ballot casting should be approximately a linear increase. If there is an influence from the promotion, there would be a tendency to deviate from the linear relationship.

The following figure depicts the difference of voter behavior between the two BM applicants.

![Fraud detection curve](https://raw.githubusercontent.com/MengXiangxi/bdwmspider/master/Fraud_detection/yafeng_vs_naiiive.png)

The figure shows that, the voter behavior of the valid BM `naiiive` is actually close to linear. However that of the deceptive BM applicant is far from linear. Horizontal axis: time lapse; verticle axis: number of ballot casted, normalized.

This result suggests that, it is extremely likely that some organized fraudulent behavior must have occurred in the voting process for the BM applicant.