sampler2D baseMap;

struct PS_INPUT 
{
   float2 Texcoord : TEXCOORD0;

};

float4 ps_main( PS_INPUT Input ) : COLOR0
{
   float4 color = tex2D( baseMap, Input.Texcoord );
   return float4(1.0f, 1.0f, 1.0f, color.w);
}

technique Technique1
{
    pass Pass1
    {
        // TODO: set renderstates here.

        //VertexShader = compile vs_2_0 VertexShaderFunction();
        PixelShader = compile ps_2_0 ps_main();
    }
}