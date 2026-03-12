import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import device, nn, optim

transforms = transforms.ToTensor() #definindo  a conversão de imagem para tensor

trainset = datasets.MNIST('./MNIST_data/', download=True, train=True, transform=transforms) #carrega a parte de treino do dataset MNIST
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True) #cria um buffer para pegar os dados por partes.

valset = datasets.MNIST('./MNIST_data/', download=True, train=False, transform=transforms) #carrega a parte de validação do dataset MNIST
valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True) #cria um buffer para pegar os dados por partes.

dataiter = iter(trainloader) #cria um iterador para o buffer de treino
# uso de next() em vez de dataiter.next() para compatibilidade com Python3
images, labels = next(dataiter) #pega a primeira parte dos dados do buffer de treino
plt.imshow(images[0].numpy().squeeze(), cmap='gray_r') #mostra a primeira imagem do buffer de treino
plt.show()  # exibe a figura

print(images[0].shape) #mostra as dimensões do tensor de imagens
print(labels[0].shape) #mostra as dimensões do tensor de rótulos

torch.Size([1, 28, 28]) #dimensões do tensor de imagens (1 canal, 28x28 pixels)
torch.size([])

class Modelo(nn.Module): #definição da classe do modelo de rede neural
    def __init__(self): #método construtor da classe
        super(Modelo, self).__init__() #chama o construtor da classe pai (nn.Module)
        self.linear1 = nn.Linear(28*28, 128) #primeira camada totalmente conectada (input: 28*28 pixels, output: 128 neurônios)
        self.linear2 = nn.Linear(128, 64) #segunda camada totalmente conectada (input: 128 neurônios, output: 64 neurônios)
        self.linear3 = nn.Linear(64, 10) #terceira camada totalmente conectada (input: 64 neurônios, output: 10 classes)

    def forward(self, x): #método de propagação para frente
        x = F.relu(self.linear1(x)) #aplica a função de ativação ReLU na saída da primeira camada
        x = F.relu(self.linear2(x)) #aplica a função de ativação ReLU na saída da segunda camada
        x = self.linear3(x) #aplica a função log_softmax na saída da terceira camada para obter as probabilidades logarítmicas das classes
        return F.log_softmax(x, dim=1)
    
def train(model, trainloader, criterion, optimizer): #função de treinamento do modelo
    otimizador = optim.SGD(model.parameters(), lr=0.01, momentum=0.5) #define o otimizador Stochastic Gradient Descent com taxa de aprendizado de 0.01
    inicio = time() #marca o início do treinamento
    
    criterio = nn.NLLLoss() #define a função de perda Negative Log Likelihood Loss
    EPOCHS = 10 #define o número de épocas para treinamento
    modelo.train() #coloca o modelo em modo de treinamento
    
    for epoch in range(EPOCHS): #loop para cada época
        perda_total = 0 #inicializa a variável de perda total
        
        for images, labels in trainloader: #loop para cada lote de imagens e rótulos no buffer de treino
            
            images = images.view(images.shape[0], -1) #reshape das imagens para um vetor de 784 elementos (28*28)
            otimizador.zero_grad() #zera os gradientes do otimizador
            
            output = model(images.to(device)) #passa as imagens pelo modelo (reshape para vetor)
            perda_instantanea = criterio(output, labels.to(device)) #calcula a perda entre a saída do modelo e os rótulos reais
            
            perda_instantanea.backward() #realiza a retropropagação para calcular os gradientes
            
            otimizador.step() #atualiza os pesos do modelo com base nos gradientes calculados
            
            perda_total += perda_instantanea.item() #acumula a perda total para a época atual
        
        else:
            print("Epoch {} - Perda resultante: {}".format(epoch+1, perda_total/len(trainloader))) #imprime a perda média por lote ao final de cada época
        print("\nTempo de treino (em minutos) =",(time()-inicio)/60) #imprime o tempo total de treinamento em minutos
        
def validacao(model, valloader, device): #função de validação do modelo
    conta_corretas, conta_todas = 0,0
    for images, labels in valloader: #loop para cada lote de imagens e rótulos no buffer de validação
        for i in range(len(labels)): #loop para cada rótulo no lote
            img = images[i].view(1, 784) #reshape da imagem para um vetor de 784 elementos (28*28)
            
            with torch.no_grad(): #desativa o cálculo de gradientes para economizar memória e acelerar a validação
                logps = model(img.to(device)) #passa a imagem pelo modelo para obter as probabilidades logarítmicas das classes
                
            ps = torch.exp(logps) #converte as probabilidades logarítmicas para probabilidades reais
            probab = list(ps.cpu().numpy()[0]) #converte as probabilidades para uma lista de numpy
            pred_label = probab.index(max(probab)) #obtém o índice da classe com a maior probabilidade
            true_label = labels.numpy()[i] #obtém o rótulo verdadeiro da imagem
            
            if(true_label == pred_label): #verifica se a previsão do modelo está correta
                conta_corretas += 1 #incrementa o contador de acertos
            conta_todas += 1 #incrementa o contador total de imagens
            
    print("Total de imagens testadas = ", conta_todas) #imprime o total de imagens testadas
    print('\nPrecisão do modelo = {:.2f}%'.format(conta_corretas/conta_todas*100)) #imprime a precisão do modelo em porcentagem
    
modelo = Modelo() #instancia o modelo de rede neural
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") #verifica se a GPU está disponível e define o dispositivo de computação
modelo.to(device) #move o modelo para o dispositivo de computação (GPU ou CPU)

Modelo(
    linear1=Linear(in_features=784, out_features=128, bias=True), linear2=Linear(in_features=128, out_features=64, bias=True), linear3=Linear(in_features=64, out_features=10, bias=True)
)