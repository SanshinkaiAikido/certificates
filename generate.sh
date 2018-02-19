if [ -e generated ]; then
	rm -rf generated
fi
mkdir generated
python3 generate.py
cd generated
for i in *.svg; do
	inkscape -z -f $i -A `basename $i svg pdf`
done
rm -f *.svg
cd ..
