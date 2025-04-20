"""
É dado um número inteiro s e um vetor crescente A[1..n] de números inteiros. 
Quero saber se existem dois elementos do vetor cuja soma é exatamente s. 
Dê um algoritmo que resolva o problema em tempo O(nlg(n)).
"""

from terceiro_modulo.divisao_e_conquista_merge_sort_for import MergeSort
from terceiro_modulo.divisao_e_conquista_busca_binaria_soma import BuscaBinariaSoma

array = [9,8,7,6,5,4,3,2,1]
soma = 10
merge_sort = MergeSort(array=array)
busca_binaria_soma = BuscaBinariaSoma(array=array, soma=soma)
print(busca_binaria_soma.result)