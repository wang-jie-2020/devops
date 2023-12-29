gitlab-runner中不包含编译环境，故考虑集成编译环境。

出于学习的目的，fork了gitlab-runner+docker+jdk+maven，在这个过程中思考的问题是在runner的环境中去搭建环境等等是否具备通用性，比如以上得镜像不能用于netcore、vue，同时即使是java项目，那么DOCKERFILE也是依据当前runner订制的，而不是只要有docker就可以构建。

本来计划做一个gitlab-runner+docker+netcore的，基于以上考虑也放弃了，我想达到的效果是只要有docker就可以构建镜像，故只做gitlab-runner+docker。

