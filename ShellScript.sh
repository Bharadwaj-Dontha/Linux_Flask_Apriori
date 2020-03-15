echo "Welcome to the Apriori Application!!"
echo ""
echo "Give Full Path of the csv file in prescribed Format"
read path
if [ -f $path ];then
	echo "Press y to give Min. Support and Min. Confidence Values ; else Press anything to continue with default values (0.3,0.6). "
	read ch
	echo $ch
	if [ $ch == "y" ]; then
		echo ""
		echo "Min. Support Value"
		read ms
		echo "Min. Confidence Value"
		read mc
		curl -X POST -F file=@$path http://bharadwajdontha00.pythonanywhere.com/upload/$ms/$mc | cat >result.txt;
	else
		curl -X POST -F file=@$path http://bharadwajdontha00.pythonanywhere.com/upload/5/3 | cat >result.txt;
	fi
	echo ""
	echo "Find the result in result.txt in Home directory"
	#cat result.txt
else
	echo "Enter valid Path"
	echo "Refer README!!"
fi



