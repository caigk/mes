
.. |bpmn en| image:: _static/images/poster-preview-bpmn-en.png
.. |Process Engine Architecture| image:: _static/images/comunda/R-C.png
.. |engine| image:: _static/images/comunda/engine.webp
    :width: 800px
.. |demo 1| image:: _static/images/comunda/demo1.png

.. _工作流演示: http://60.205.152.250/
.. _camunda: https://camunda.com/

#############################
 `Camunda`_
#############################


*****************************
参考资料
*****************************

.. |camunda.com| image:: https://img.shields.io/badge/www-camunda-blue?logo=camunda
  :target: https://www.camunda.com/

.. |start.camunda.com| image:: https://img.shields.io/badge/start-comunda-blue?logo=camunda
  :target: https://start.camunda.com/

.. |camunda docs 7.22| image:: https://img.shields.io/badge/docs-camunda_7.22-blue?logo=
  :target: https://docs.camunda.org/manual/7.22/

.. |camunda github| image:: https://img.shields.io/badge/github-camunda-blue?logo=github
  :target: https://github.com/camunda/
.. |camunda examples github| image:: https://img.shields.io/badge/github-camunda_examples-blue?logo=github
  :target: https://github.com/camunda/camunda-bpm-examples
.. |pycamunda| image:: https://img.shields.io/badge/github-pycamunda-blue?logo=github
  :target: https://github.com/pklauke/pycamunda
.. |camunda external task client js| image:: https://img.shields.io/badge/github-external_client_js-blue?logo=github
  :target: https://github.com/camunda/camunda-external-task-client-js



* |camunda.com| |start.camunda.com|
* |camunda docs 7.22| 
* |camunda github| |camunda examples github|··
* |camunda external task client js| |pycamunda|

.. tip::
  注意：-ee 表示 "enterprice edition" 企业版，可能不能使用!

**文章**

* `How to choose the right Camunda architecture. <https://camunda.com/blog/2020/04/how-to-choose-the-right-camunda-architecture/>`_

**常用**

* `org.camunda.bpm.engine javadoc <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.22/org/camunda/bpm/engine/package-summary.html>`_
* `org.camunda.bpm.spring.boot.starter javadoc <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.22/org/camunda/bpm/spring/boot/starter/package-summary.html>`_

================================
 若依/RuoYi-Vue
================================

* `工作流演示`_ 
* `Example <https://example.com/>`_

*****************************
基础
*****************************

===============================
Process Engine Architecture
===============================

 |Process Engine Architecture|
 |engine|

================================
bpmn
================================

|bpmn en|

*****************************
常用代码
*****************************

下载：`camunda release <https://downloads.camunda.cloud/release/>`_

=============================
camunda-bpm-tomcat
=============================

.. code-block::
  :caption: 下载安装

    #下载安装
    wget https://downloads.camunda.cloud/release/camunda-bpm/tomcat/7.22/camunda-bpm-tomcat-7.22.0.tar.gz
    tar -zxvf camunda-bpm-tomcat-7.22.0.tar.gz
    #启动
    ./camunda-bpm-tomcat-7.22.0/start-camunda.
    #发布war包至目录不:server/apache-tomcat-10.1.30/webapps/

=============================
camunda-bpm-examples
=============================
.. code-block::
  :caption: 下载安装

    #下载安装
    git clone https://github.com/camunda/camunda-bpm-examples
    
.. tip::
  注意： 一定要使用使用Java 17


*****************************
其它
*****************************

|demo 1|

