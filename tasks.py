from invoke import task


@task
def format(ctx):
    ctx.run("black .")


@task
def test(ctx):
    ctx.run("pytest")


@task
def docker_build(ctx):
    ctx.run("docker build . --tag ingester")


@task(docker_build)
def docker_deploy(ctx):
    ctx.run("docker stack deploy --compose-file docker-compose.yaml ingester")


@task
def docker_stop(ctx):
    ctx.run("docker stack rm ingester")


@task
def docker_logs(ctx, service="consumer"):
    ctx.run(f"docker service logs ingester_{service} --follow")
