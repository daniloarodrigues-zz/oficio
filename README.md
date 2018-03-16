<h1>Gerador de Ofícios</h1>
<h2>Sistema para geração e controle de emissão de ofícios do Poder Legislativo.</h2>


<h4>O que é?</h4>
<p>O Beta4 é um sistema experimental de geração de ofícios do Poder Legislativo. Seu desenvolvimento inicial se deu devido a falta de padronização e de local para armazenar ofícios da Câmara Municipal do Jaboatão dos Guararapes/PE. Então para agilizar e facilitar o processo de criação e armazenamento dos ofícios gerados pela Casa Legislativa idealizei o sistema de forma que todos os gabinetes e setores da Câmara pudessem utilizar o sistema. Com ele, o órgão pode criar usuários para determinados setores que terão acesso ao sistema podendo gerar ofícios numerados que são organizados em ordem crescente, e ficam armezenados em um servidor local podendo ser acessados de qualquer dispositivo (PC, Tablet, Celular e outros equipamentos com internet).</p>

<h4>Quem pode usar?</h4>
<p>Qualquer entidade, seja pessoa física ou jurídica, que queira um sistema de geração de documentos. Embora o sistema esteja personalizado para gerar ofícios do Poder Legislativo, ele é facilmente customizável, e pode ser utilizado para qualquer outro tipo de documento.</p>

<h4>Qualquer um consegue fazer as configurações iniciais?</h4>
<p>O objetivo é facilitar o máximo para que não haja dificuldades na implementação do mesmo. Para isso, disponibilizamos um vídeo mais abaixo que explica de forma simples e rápida como implementar o sistema em uma rede local.</p>
<p>Embora não seja difícil fazer a implantação do sistema, é necessário que o responsável tenha alguns conhecimentos básicos:</p>
<pre>
    <p>Saber criar containers no docker - (Necessário para fazer a instalação do container com nosso <a href="https://github.com/daniloarodrigues/oficio/blob/master/docker-compose.yml">docker-compose.yml</a>)</p>
    <p>Saber usar os comandos básicos do terminal linux - (Necessário para se movimentar entre pastas e fazer instalaçãos de pacotes)</p>
    <p>Saber os comandos básicos do virtualenv - (Necessário para ativar a máquina virtual e subir a aplicação com gunicorn)</p>
    <p>Saber o básico do nginx - (Necessário para fazer a configuração mais básica do <a href="https://github.com/daniloarodrigues/oficio/blob/master/default.conf">nginx</a>)</p>
</pre>
<p>Conhecimentos recomendados <b>(Não obrigatórios)</b>:</p>
<pre>
    <p>Saber o básico de configurações de dns - (Necesários para adicionar um domínio para acessar o sistema)</p>
</pre>