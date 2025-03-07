using Emgu.CV;
using Emgu.CV.CvEnum;
using OuterSpaceDetection.WebApi.Application.Services;

namespace OuterSpaceDetection.WebApi.Infrastructure.Services;

public sealed class OpenCVService : IOpenCVService
{
    public async Task<Mat> ProcessImageAsync(string imagePath,CancellationToken cancellationToken)
    {
        Mat img = await Task.Run(() => CvInvoke.Imread(imagePath, ImreadModes.Color), cancellationToken);
        return img;
    }
}
