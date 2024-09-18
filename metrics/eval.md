We provide two methods for evaluating the quality of generation  
[`AIGCBench`](https://github.com/BenchCouncil/AIGCBench) for image to video evaluation, 
[`EvalCrafter`](https://github.com/evalcrafter/evalcrafter) for text to video evaluation   


Combining the two approaches, the following assessment indicators are provided.

<table>
    <tr>
        <th>Aspects</th>
        <th>Metrics</th>
        <th>T2V</th>
        <th>I2V</th>
        <th>Method</th>
    </tr>
    <tr>
        <td rowspan="2">Quantity</td>   
        <td>IS</td>
        <td>√</td>
        <td>√</td>
        <td>AIGCBench</td>
    </tr>
    <tr>
        <td>VQA</td>
        <td>√</td>
        <td>√</td>
        <td>EvalCrafter VQA-T, VQA-A</td>
    </tr>
    <tr>
        <td rowspan="2">Temporal Consistency</td>
        <td>temporal</td>
        <td>√</td>
        <td>√</td>
        <td>EvalCrafter CLIP-Temp</td>
    </tr>
    <tr>
        <td>warping error</td>
        <td>√</td>
        <td>√</td>
        <td>EvalCrafter warping error</td>
    </tr>
    <tr>
        <td>Motion</td>
        <td>flow score</td>
        <td>√</td>
        <td>√</td>
        <td>EvalCrafter flow scor</td>
    </tr>
    <tr>
        <td rowspan="3">Image-Video Alignment</td>
        <td>MSE</td>
        <td>×</td>
        <td>√</td>
        <td>AIGCBench MSE(First)</td>
    </tr>
    <tr>
        <td>SSIM</td>
        <td>×</td>
        <td>√</td>
        <td>AIGCBench SSIM(First) </td>
    </tr>
    <tr>
        <td>IV-CLIP</td>
        <td>×</td>
        <td>√</td>
        <td>AIGCBench Image-GenVideo clip</td>
    </tr>
    <tr>
        <td rowspan="3">Text-Video Alignment</td>
        <td>TV-CLIP</td>
        <td>√</td>
        <td>×</td>
        <td>EvalCrafter</td>
    </tr>
    <tr>
        <td>blip bleu</td>
        <td>√</td>
        <td>×</td>
        <td>EvalCrafter</td>
    </tr>
    <tr>
        <td>sd score</td>
        <td>√</td>
        <td>×</td>
        <td>EvalCrafter</td>
    </tr>
</table>