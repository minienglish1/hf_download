source venv/bin/activate
while true
do
python download.py --model Salesforce/instructblip-flan-t5-xl
python download.py --model Salesforce/instructblip-flan-t5-xxl
python download.py --model Salesforce/instructblip-vicuna-13b
python download.py --model Salesforce/instructblip-vicuna-7b
done
