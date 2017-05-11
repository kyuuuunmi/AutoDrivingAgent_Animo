
#! /bin/bash

#python serial_test.py

control_4() {
	echo "In Control 4 =============="
	b_pid=$!
	kill $b_pid
	echo "finish"
	python ReleaseController.py
#	jobs
#	fg %1
#	echo "fg %1 ================"
#	sudo service motion stop
#	echo "motion stop"
	exit
}

trap control_4 SIGQUIT

sudo service motion start


echo "[python] Backgroud Process Start --- ================="
python MainController.py &

#sleep 5

#echo "Start -> jobs*********************************"
#jobs
#b_pid=$!
#kill $b_pid
#echo "After Kill -> jobs\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
#jobs

#echo "!!!!!!!!!!!"
#fg %1
#echo "@@@@@@@@@@@"
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.78.63.210:8008/darknet

while true
do
	scp -i /home/animo02/secret/soptAMSKey.pem -r /var/lib/motion/ ubuntu@52.78.63.210:/home/ubuntu/CNN
	sudo rm -rf /var/lib/motion/*.jpg | sudo rm -rf /var/lib/motion/*.avi
done


