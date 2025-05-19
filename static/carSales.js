document.addEventListener('DOMContentLoaded', () => {
    // Seleciona todos os botões na página
    const buttons = document.querySelectorAll('button');

    for (const button of buttons) {
        button.addEventListener('click', () => {
            // tenta obter os atributos data-name e data-brand do botão
            const carName = button.getAttribute('car') || 'Nome desconhecido';
            const carBrand = button.getAttribute('brand') || 'Marca desconhecida';

            alert(`O carro ${carName} da marca ${carBrand} foi vendido.`);
        });
    }
});