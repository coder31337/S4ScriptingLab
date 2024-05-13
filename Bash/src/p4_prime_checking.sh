read -p "Enter a number " NUM
IS_PRIME=0
if [ $NUM -gt 1 ] ; then
    IS_PRIME=1
    for (( i=2; i<=NUM/2; i++ )) ; do
        if [ $((NUM%i)) -eq 0 ] ; then
            IS_PRIME=0
        fi
    done
fi

if [ $IS_PRIME -eq 1 ] ; then
    echo "Entered number is a prime"
else
    echo "Entered number is not a prime"
fi
