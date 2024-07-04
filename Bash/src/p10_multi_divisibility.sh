read -p "Enter a number: " NUM

if [ $((NUM%3)) -eq 0 ] ; then
    echo "Number is divisible by 3"
else
    echo "Number is not divisible by 3"
fi
if [ $((NUM%4)) -eq 0 ] ; then
    echo "Number is divisible by 4"
else
    echo "Number is not divisible by 4"
fi
if [ $((NUM%5)) -eq 0 ] ; then
    echo "Number is divisible by 5"
else
    echo "Number is not divisible by 5"
fi
