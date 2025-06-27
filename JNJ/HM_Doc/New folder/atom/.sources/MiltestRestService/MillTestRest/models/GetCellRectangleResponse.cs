using System.Drawing;

namespace MillTestRest.models
{
    public record GetCellRectangleResponse
    {
        public Rect? rectangle {  get; set; }
    }
}
