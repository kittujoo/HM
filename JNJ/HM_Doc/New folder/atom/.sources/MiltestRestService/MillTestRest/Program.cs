using Microsoft.AspNetCore.Mvc;
using MillTestRest.models;
using MillTestRest.milltest;
using System.Text;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();



app.MapPost("/getCellText", ([FromHeader] int handle, [FromBody] GetCellTextRequest dto) =>
{
    var builder = new StringBuilder();
    var output = MiltestDllUtil.GetCellText(handle, dto.row, dto.column, builder);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Cell with coordinates: [column: {dto.column}, row: {dto.row}] not found", handle = handle });


    return Results.Ok(new GetCellTextResponse() { text = builder.ToString() });
});

app.MapPost("/setCellText", ([FromHeader] int handle, [FromBody] SetCellTextRequest dto) =>
{
    var output = MiltestDllUtil.SetCellText(handle, dto.row, dto.column, dto.text);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Cell with coordinates: [column: {dto.column}, row: {dto.row}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/makeCellVisible", ([FromHeader] int handle, [FromBody] MakeCellInvisibleRequest dto) =>
{
    var output = MiltestDllUtil.MakeCellVisible(handle, dto.row, dto.column);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Cell with coordinates: [column: {dto.column}, row: {dto.row}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/getCellRectangle", ([FromHeader] int handle, [FromBody] GetCellRectangleRequest dto) =>
{
    var rect = new Rect();
    var output = MiltestDllUtil.WhereIsCell(handle, dto.row, dto.column, ref rect);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Cell with coordinates: [column: {dto.column}, row: {dto.row}] not found", handle = handle });

    return Results.Ok(new GetCellRectangleResponse() { rectangle = rect });
});

app.MapPost("/getColumnIndex", ([FromHeader] int handle, [FromBody] GetColumnIndexRequest dto) =>
{
    var output = MiltestDllUtil.GetColumnNum(handle, dto.columnName);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Column with name [{dto.columnName}] not found", handle = handle });

    return Results.Ok(new GetColumnIndexResponse() { columnIndex = output });
});

app.MapPost("/isColumnHidden", ([FromHeader] int handle, [FromBody] IsColumnHiddenRequest dto) =>
{
    var output = MiltestDllUtil.IsColumnHidden(handle, dto.columnIndex);

    return Results.Ok(new IsColumnHiddenResponse() { isHidden = Convert.ToBoolean(output) });
});

app.MapPost("/selectAndShowColumn", ([FromHeader] int handle, [FromBody] SelectAndShowColumnRequest dto) =>
{
    var output = MiltestDllUtil.SelectAndShowColumn(handle, dto.columnIndex);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Column with index [{dto.columnIndex}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/selectColumn", ([FromHeader] int handle, [FromBody] SelectColumnRequest dto) =>
{
    var output = MiltestDllUtil.SelectColumn(handle, dto.columnIndex);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Column with index [{dto.columnIndex}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/showColumn", ([FromHeader] int handle, [FromBody] ShowColumnRequest dto) =>
{
    var output = MiltestDllUtil.ShowColumn(handle, dto.columnIndex);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Column with index [{dto.columnIndex}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/deselectColumn", ([FromHeader] int handle, [FromBody] DeselectColumnRequest dto) =>
{
    var output = MiltestDllUtil.DeselectColumn(handle, dto.columnIndex);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Column with index [{dto.columnIndex}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/getTabNumber", ([FromHeader] int handle, [FromBody] GetTabNumberRequest dto) =>
{
    var output = MiltestDllUtil.GetTabNum(handle, dto.tabName);
    if (output < 0)
        return Results.NotFound(new ErrorResponse() { message = $"Tab with name [{dto.tabName}] not found", handle = handle });


    return Results.Ok(new GetTabNumberResponse() { tabIndex = output });
});

app.MapPost("/selectTabByIndex", ([FromHeader] int handle, [FromBody] SelectTabByIndexRequest dto) =>
{
    var output = MiltestDllUtil.SelectTabNum(handle, dto.tabIndex);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Tab with index [{dto.tabIndex}] not found", handle = handle });

    return Results.Ok();
});

app.MapPost("/selectTabByTitle", ([FromHeader] int handle, [FromBody] SelectTabByTitleRequest dto) =>
{
    var output = MiltestDllUtil.SelectTabTitle(handle, dto.tabTitle);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Tab with title [{dto.tabTitle}] not found" });

    return Results.Ok();
});

app.MapPost("/getTabText", ([FromHeader] int handle, [FromBody] GetTabTestRequest dto) =>
{
    var builder = new StringBuilder();
    var output = MiltestDllUtil.GetTabText(handle, dto.tabIndex, builder);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"Tab with index [{dto.tabIndex}] not found", handle = handle });

    return Results.Ok(new GetTabTextResponse() { text = builder.ToString() });
});

app.MapPost("/getTabsCount", ([FromHeader] int handle) =>
{
    var output = MiltestDllUtil.NumTabs(handle);

    if (output <= 0)
        return Results.NotFound(new ErrorResponse() { message = $"No tabs found", handle = handle });

    return Results.Ok(new GetTabCountResponse() { count = output });
});


app.MapPost("/getCurrentTab", ([FromHeader] int handle) =>
{
    var output = MiltestDllUtil.GetCurrentTab(handle);

    if (output < 0)
        return Results.NotFound(new ErrorResponse() { message = $"Not tabs found", handle = handle });

    return Results.Ok(new GetCurrentTabResponse() { tabIndex = output });
});

app.Run();