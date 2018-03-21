if [ -e output ]; then
	rm -rf output
fi
mkdir output
python3 convert.py
cd output
for i in *.svg; do
	echo 'Generating '`basename $i svg`pdf
	inkscape -z -f $i -A `basename $i svg`pdf
done
rm -f *.svg
ls *pdf|wc -l
cd ..
zip -r certificates-`date +%Y%m%d%H%M`.zip output
