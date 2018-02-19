if [ -e output ]; then
	rm -rf output
fi
mkdir output
python3 convert.py
cd output
for i in *.svg; do
	inkscape -z -f $i -A `basename $i svg`pdf
done
rm -f *.svg
cd ..
