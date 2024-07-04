read -p "Enter a number: " NUM
FACT=1
for (( i=1; i<=NUM; i++ )) ; do
    FACT=$((FACT*i))
done
echo "Factorial is $FACT"
