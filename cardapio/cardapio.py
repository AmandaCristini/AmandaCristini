from prato import Prato

class Cardapio():

  def __init__(self, cardapio = []):
    self.cardapio = cardapio


  def cadastrar_prato(self, prato):
    cadastro = input('Deseja cadastrar um prato? s/n\n> ')
    if cadastro == 's' :
      self.cardapio.append(prato)
      print('Prato cadastrado')
    else:
      print('Obrigada')

def exibir():
  for i in card.cardapio:
    print(f'Nome:{i.nome}\nDescrição:{i.descricao}\nPreço:{i.preco}\n')
  return card.cardapio


card = Cardapio()
prato1 = Prato("Pizza Calabresa", "Pizza sabor calabresa", 55.00)
prato2 = Prato("Macarrão", "Massa penne com molho 4 queijos", 40.00)
prato3 = Prato("Só quero chocolate", "Sorvete de chocolate amargo com cobertura de chocolate ao leite e pedaços de chocolate branco", 23)
card.cadastrar_prato(prato1)
card.cadastrar_prato(prato2)
card.cadastrar_prato(prato3)
print(exibir())
