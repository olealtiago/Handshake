# TCP 3-Way Handshake

O nosso primeiro desafio irá envolver muitos conceitos interessantes, inciaremos
com a instalação do Docker e do Docker-compose para podemos executar containers
na nossa máquina de trabalho. Em seguida, iremos entender como utilizar o Scapy
para criacão e envio de pacotes através da rede para isso,  utilizaremos o
Wireshark para observar os pacotes que trafegam em uma rede de computadores. 
Por fim, teremos o desafio final, implementar preparar um paco de Layer 4
para realizar o processo de Handshake no protocolo TCP.

# Docker
Para facilitar, deixei um script para instalar o docker e o docker-compose na versão
adequada. Para instalá-los execute:

```sh
./scripts/install_docker.sh
```

Se não precisar instalar o Docker e só precisar instalar o Compose, favor utilizar:
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

# Scapy
Link para a documentação do Scapy:

[https://scapy.readthedocs.io/en/latest/](https://scapy.readthedocs.io/en/latest/)

# Wireshark
Recomendo a utilização do Wireshark para debug dos pacotes na rede, se preferir
pode utilizar tcpdump.

Para instalar o Wireshark:
```sh
sudo apt -y install wireshark
```

Se só for possível ver as interfaces utilizando 'sudo', reconfigure o wireshark da
[seguinte forma](https://askubuntu.com/questions/74059/how-do-i-run-wireshark-with-root-privileges).

# Desenvolvimento

Para executar os containers e criar a rede, invoque docker-compose com o compando up.

```sh
docker-compose up
```

Para matar os containers aperte CTRL + c no terminal onde o compose foi executado. Se CTRL + c for pressionado duas vezes o container irá parar forçadamente, fique a vontade para fazer dessa forma.

O desenvolvimento deve ser feito na pasta scripts, no arquivo solution.py, fique a vontade para criar funções, classes, documentar a sua implementação e fazer uso de boas práticas de desenvolvimento.
O desenvolvimento não precisa ser feito dentro do container! Abra o arquivo solution.py no seu editor de preferência e somente conecte no container cliente para executar o script.

Para executar o script que se conecta ao container:

```sh
./scripts/connect_to_client.sh
``` 

Para executar o script, execute DENTRO DO CONTAINER:

```sh
./scripts/solution.py
```

# Referências sobre TCP Handshake

Seguem algumas referências simples sobre TCP Handshake, fiquem a vontade para pesquisar
o que quiserem na rede, evitem usar os termos 'Scapy + TCP + Handshake'

[https://gitbook.ganeshicmc.com/redes/three-way-handshake](https://gitbook.ganeshicmc.com/redes/three-way-handshake)

[https://www.geeksforgeeks.org/tcp-3-way-handshake-process/](https://www.geeksforgeeks.org/tcp-3-way-handshake-process/)
