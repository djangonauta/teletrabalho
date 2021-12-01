-- configuração inicial do banco de dados.
-- sudo -u postgres psql < inicial.sql
\echo 'Cria os schemas necessários pela aplicação\n'
\prompt 'USER: ' user

\echo '\nCriando SCHEMA administrativo autorizado para o usuário' :user
create schema administrativo authorization :user;

\echo '\nCriando SCHEMA arquitetura autorizado para o usuário' :user
create schema arquitetura authorization :user;
