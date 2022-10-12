#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EOE(pt, msg, returnCode) \
  if ((pt) == NULL) { \
    printf(msg);
    return (returnCode);\
  }

// #define XP_WIN for Windows and
#define XP_UNIX // for UNIX systems

// Include the main JS-API with these directives. It is important to 
// set the operating system **before** including these headers. They
// are located in the js/src/ directory of the SpiderMonkey/1.8 release.
#include "jsapi.h"
#include "jsxdrapi.h"

int main(int argc, char const *argv[])
{
  JSRuntime *runtime;
  JSContext *ctx;
  JSObject  *global;
  JSScript  *script;

  JSBool status;
  jsval  result;

  long runtimeSize = 8;//MegaByte

  JSClass jc_Global = {
    "global", JSCLASS_HAS_PRIVATE, JS_PropertyStub,
    JS_PropertyStub, JS_PropertyStub, JS_PropertyStub,
    JS_EnumerateStub, JS_ResolveStub, JS_FinalizeStub,
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0
  };

  runtime = JS_NewRuntime(runtimeSize * 1024L * 1024L);
  EOE(runtime, "Could not initialize JavaScript-Runtime", 1)

  ctx = JS_NewContext(runtime, 8192);
  EOE(ctx, "Could not initialize JavaScript-Context", 2)

  global = JS_NewObject(ctx, &jc_Global, NULL, NULL);
  EOE(runtime, "Could not initialize JavaScript global object", 3)
  
  status = JS_InitStandardClasses(ctx, global);
  if (status == JS_FALSE) {
    printf("Could not load standard classes");
    return 4;
  }

  JSXDRState *xdrMemory = JS_XDRNewMem(ctx, JSXDR_DECODE);
  EOE(xdrMemory, "Could not initialize memory for XDR-Script", 5)

  void *fp = fopen(argv[1], "rb");
  EOE(fp, "Could not open file", 6)

  fseek(fp, 0, SEEK_END);
  int length = ftell(fp);
  fseek(f, 0, SEEK_SET);

  void *data = malloc((size_t) length);
  EOE(data, "Could not allocate memory for file data", 7)

  fread(data, 1, length, fp);
  JS_XDRMemSetData(xdr, data, length);
  if (JS_XDRScript(xdr, &script) != JS_TRUE) {
    printf("Could not decompile XDR-Script");
    return 8;
  }

  JSString *src = JS_DecompileScript(ctx, script, "decompiled.js", 2);
  char *sourcecode = JS_GetStringBytes(src);

  printf("%s", sourcecode);

  // Cleanup
  JS_DestroyContext(ctx);
  JS_DestroyRuntime(runtime);
  return 0;

}
