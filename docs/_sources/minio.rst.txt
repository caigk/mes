#############################
 MinIO
#############################

*****************************
参考资料
*****************************

`MinIO <https://min.io/>`_

*****************************
常用代码
*****************************

=============================
docker
=============================

.. code-block::
  :caption: Docker使用

    #拉取
    docker pull minio/MinIO

    #启动
    docker run -p 9000:9000 -p 9090:9090 \
            --name minio \
            -d --restart=always \
            -e "MINIO_ACCESS_KEY=minio" \
            -e "MINIO_SECRET_KEY=minio123" \
            -v /Users/zhouchenghuan/mydata/minio/data:/data \
            minio/minio server \
            /data --console-address ":9090" -address ":9000"
    
    #打开
    #http://localhost:9090