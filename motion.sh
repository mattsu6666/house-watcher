sleep 10
v4l2-ctl --set-ctrl=white_balance_auto_preset=0
python /home/pi/mail_motion_start.py
/usr/bin/motion -c /etc/motion/motion.conf