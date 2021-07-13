sampler s0; 
float ColLevel;
float ColR, ColG, ColB;


float4 PixelShaderFunction(float2 coords: TEXCOORD0) : COLOR0
{
   float4 Color = tex2D(s0, coords.xy);

   if (Color.a > 0) 
   {
	   if (ColR > Color.r)
			Color.r = (ColR - Color.r) * ColLevel + Color.r;
	   else
			Color.r = Color.r - (Color.r - ColR) * ColLevel;

	   if (ColG > Color.g)
			Color.g = (ColG - Color.g) * ColLevel + Color.g;
	   else
			Color.g = Color.g - (Color.g - ColG) * ColLevel;

	   if (ColB > Color.b)
			Color.b = (ColB - Color.b) * ColLevel + Color.b;
	   else
			Color.b = Color.b - (Color.b - ColB) * ColLevel;
   }

   //Color.rgb = float3(param1,Color.g,Color.b); 
   return Color;
}

float4 PixelShaderFunction2(float2 coords: TEXCOORD0) : COLOR0
{
   float4 Color = tex2D(s0, coords.xy);
   return Color;
}

technique Technique1
{
    pass Pass1
    {
        PixelShader = compile ps_2_0 PixelShaderFunction();
    }
}

