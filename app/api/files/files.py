from app.api.route import get_router
from fastapi import FastAPI, File, UploadFile
from typing import List

files_router = get_router()

path = r'F:\02_data\test'

@files_router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    tmp_pth = r'%s/%s' % (path, file.filename)

    # Open a file
    with open(tmp_pth,"wb+") as f:
        f.write(contents)
    return {
        "file_size": len(contents),
        "file_name": file.filename
    }






@files_router.post("/uploadfiles/")
async def upload_file(tempfiles: List[UploadFile] = File(...)):
    for tempfile in tempfiles:
        tmp_pth = r'%s/%s'%(path,tempfile.filename)
        print(tmp_pth)
        #f"/opt/{tempfile.filename}"
        with open(tmp_pth, 'wb') as f:
            for i in iter(lambda : tempfile.file.read(1024*1024*100),b''):
                f.write(i)
        f.close()
    return {"files_name":[x.filename for x in tempfiles]}

from fastapi.responses import HTMLResponse
@files_router.get("/file")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


#静态文件代理的第二种方法
from fastapi.responses import FileResponse
@files_router.get("/static1")
async def main():
    some_file_path = r"E:\01_proj\003_backup\000_work.rar"
    return FileResponse(some_file_path)



