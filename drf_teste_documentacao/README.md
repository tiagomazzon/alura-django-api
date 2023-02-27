# [Curso de API com Django 3: Aprofundando em testes e documentação](https://cursos.alura.com.br/course/api-django-3-testes-documentacao)

* Aprendemos que é possível carregar dados iniciais para os modelos através das fixtures. Para isso, dentro de cada APP, podemos criar uma pasta chamada fixtures com dados no formato JSON, por exemplo, e carregá-los executando o comando manage.py loaddata seguido do nome do arquivo que contém os dados.
* Aprendemos que existem diferentes formas de testar uma aplicação, como testes manuais, automatizados, testes de unidade, integração, entre outros.
* Aprendemos que o teste de unidade é um método de teste de software no qual os componentes individuais do programa, chamados de unidades, são testados a despeito das dependências necessárias;
* Criamos os testes de unidade para verificar os campos serializados e se o modelo atribuía os valores default quando eram omitidos.
* Criamos os testes que verificam a autenticação de um usuário com base nas políticas de acesso do Django, criando um usuário na base de dados de testes;
* Verificamos as tentativas de acesso de um usuário com as credenciais corretas e incorretas e realizamos uma requisição GET de um usuário autenticado.
* Aprendemos que é possível carregar os dados das fixtures no banco de dados de testes;
* Testamos a API da Alura no Postman, verificando se o statuscode da requisição era o esperado. Além disso, verificamos também se o tipo de dado da resposta estava no formato desejado.
* Entendemos a importância de documentar uma API para outras pessoas e sistemas. Porém, essa documentação deve seguir o ritmo da implementação de código;
* Integramos o Swagger no Django Rest Framework e vimos na prática a documentação gerada. Além disso, realizamos alguns testes no Swagger.