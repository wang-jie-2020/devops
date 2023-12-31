# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ARG version

FROM apache/skywalking-base:${version}-es6 AS build

WORKDIR skywalking

RUN set -eux; \
    rm -rf "config"; rm -rf "oap-libs"; \
    rm -rf "agent";

COPY docker-entrypoint.sh .
COPY logback.xml webapp/

FROM adoptopenjdk/openjdk11:alpine

ENV JAVA_OPTS=" -Xms256M " \
    SW_OAP_ADDRESS="http://oap:12800" \
    SW_TIMEOUT="20000"

LABEL maintainer="hanahmily@apache.org,tanjian@apache.org"

COPY --from=build /skywalking /skywalking

WORKDIR skywalking

RUN apk add --no-cache \
    bash

EXPOSE 8080

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
