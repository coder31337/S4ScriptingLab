LARGEST=$1
if [ $2 -gt $LARGEST ] ; then
    LARGEST=$2
fi
if [ $3 -gt $LARGEST ] ; then
    LARGEST=$3
fi
FACT=1
for (( i=1; i<=LARGEST; i++ )) ; do
    FACT=$((FACT*i))
done
echo "Factorial of $LARGEST is $FACT"
