echo " BUILD START"
python3.9 -m pip install -r requeriments.txt
python3.9 -m manage.py collectstatic --noinput --clear
echo " BUILD END"