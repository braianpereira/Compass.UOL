#3 – Crie um Shell Script para automatizar alguma tarefa em ambiente GNU/Linux e me envie para ter um feedbac

#!/bin/bash
echo "Taboada"
echo "Informe um numero de ver a sua taboada"
read NUMERO
for i in `seq 1 10`
do
    mult=$(($i * $NUMERO))
    echo  "$i" X $NUMERO = $mult
done