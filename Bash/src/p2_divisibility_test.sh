read -p "Enter a number: " NUM

if [ $((NUM%5)) -eq 0 ] ; then
    echo "Number is divisible by 5"
else
    echo "Number is not divisible by 5"
fi
