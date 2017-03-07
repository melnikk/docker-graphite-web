build:
	docker build . -t skbkontur/graphite-web:alpine-graphite-master

start:
	ansible-playbook -i "localhost," ansible.yml --become
