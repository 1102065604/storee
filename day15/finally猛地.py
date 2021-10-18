

try:
    print("机器正常启动！")
    print("机器正常运转！")
    raise SystemError("电压不稳定！系统错误！")

except Exception as e:
    print("异常处理完成，别担心！", e.args)
finally:  # 最终的意思，finally不管有没有异常报错，他肯定会执行。
    try:
        print("机器正常关闭！")
        raise SystemError("没有正常关闭！")
    except Exception:
        print("强行正常关闭！")

















