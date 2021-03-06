#!/usr/bin/env python
"""CLI for bigquery, version v2."""
# NOTE: This file is autogenerated and should not be edited by hand.

import code
import os
import platform
import sys

from apitools.base.protorpclite import message_types
from apitools.base.protorpclite import messages

from google.apputils import appcommands
import gflags as flags

import apitools.base.py as apitools_base
from apitools.base.py import cli as apitools_base_cli
import bigquery_v2_client as client_lib
import bigquery_v2_messages as messages


def _DeclareBigqueryFlags():
  """Declare global flags in an idempotent way."""
  if 'api_endpoint' in flags.FLAGS:
    return
  flags.DEFINE_string(
      'api_endpoint',
      u'https://www.googleapis.com/bigquery/v2/',
      'URL of the API endpoint to use.',
      short_name='bigquery_url')
  flags.DEFINE_string(
      'history_file',
      u'~/.bigquery.v2.history',
      'File with interactive shell history.')
  flags.DEFINE_multistring(
      'add_header', [],
      'Additional http headers (as key=value strings). '
      'Can be specified multiple times.')
  flags.DEFINE_string(
      'service_account_json_keyfile', '',
      'Filename for a JSON service account key downloaded'
      ' from the Developer Console.')
  flags.DEFINE_enum(
      'alt',
      u'json',
      [u'json'],
      u'Data format for the response.')
  flags.DEFINE_string(
      'fields',
      None,
      u'Selector specifying which fields to include in a partial response.')
  flags.DEFINE_string(
      'key',
      None,
      u'API key. Your API key identifies your project and provides you with '
      u'API access, quota, and reports. Required unless you provide an OAuth '
      u'2.0 token.')
  flags.DEFINE_string(
      'oauth_token',
      None,
      u'OAuth 2.0 token for the current user.')
  flags.DEFINE_boolean(
      'prettyPrint',
      'True',
      u'Returns response with indentations and line breaks.')
  flags.DEFINE_string(
      'quotaUser',
      None,
      u'Available to use for quota purposes for server-side applications. Can'
      u' be any arbitrary string assigned to a user, but should not exceed 40'
      u' characters. Overrides userIp if both are provided.')
  flags.DEFINE_string(
      'trace',
      None,
      'A tracing token of the form "token:<tokenid>" to include in api '
      'requests.')
  flags.DEFINE_string(
      'userIp',
      None,
      u'IP address of the site where the request originates. Use this if you '
      u'want to enforce per-user limits.')


FLAGS = flags.FLAGS
apitools_base_cli.DeclareBaseFlags()
_DeclareBigqueryFlags()


def GetGlobalParamsFromFlags():
  """Return a StandardQueryParameters based on flags."""
  result = messages.StandardQueryParameters()
  if FLAGS['alt'].present:
    result.alt = messages.StandardQueryParameters.AltValueValuesEnum(FLAGS.alt)
  if FLAGS['fields'].present:
    result.fields = FLAGS.fields.decode('utf8')
  if FLAGS['key'].present:
    result.key = FLAGS.key.decode('utf8')
  if FLAGS['oauth_token'].present:
    result.oauth_token = FLAGS.oauth_token.decode('utf8')
  if FLAGS['prettyPrint'].present:
    result.prettyPrint = FLAGS.prettyPrint
  if FLAGS['quotaUser'].present:
    result.quotaUser = FLAGS.quotaUser.decode('utf8')
  if FLAGS['trace'].present:
    result.trace = FLAGS.trace.decode('utf8')
  if FLAGS['userIp'].present:
    result.userIp = FLAGS.userIp.decode('utf8')
  return result


def GetClientFromFlags():
  """Return a client object, configured from flags."""
  log_request = FLAGS.log_request or FLAGS.log_request_response
  log_response = FLAGS.log_response or FLAGS.log_request_response
  api_endpoint = apitools_base.NormalizeApiEndpoint(FLAGS.api_endpoint)
  additional_http_headers = dict(x.split('=', 1) for x in FLAGS.add_header)
  credentials_args = {
      'service_account_json_keyfile': os.path.expanduser(FLAGS.service_account_json_keyfile)
  }
  try:
    client = client_lib.BigqueryV2(
        api_endpoint, log_request=log_request,
        log_response=log_response,
        credentials_args=credentials_args,
        additional_http_headers=additional_http_headers)
  except apitools_base.CredentialsError as e:
    print 'Error creating credentials: %s' % e
    sys.exit(1)
  return client


class PyShell(appcommands.Cmd):

  def Run(self, _):
    """Run an interactive python shell with the client."""
    client = GetClientFromFlags()
    params = GetGlobalParamsFromFlags()
    for field in params.all_fields():
      value = params.get_assigned_value(field.name)
      if value != field.default:
        client.AddGlobalParam(field.name, value)
    banner = """
           == bigquery interactive console ==
                 client: a bigquery client
          apitools_base: base apitools module
         messages: the generated messages module
    """
    local_vars = {
        'apitools_base': apitools_base,
        'client': client,
        'client_lib': client_lib,
        'messages': messages,
    }
    if platform.system() == 'Linux':
      console = apitools_base_cli.ConsoleWithReadline(
          local_vars, histfile=FLAGS.history_file)
    else:
      console = code.InteractiveConsole(local_vars)
    try:
      console.interact(banner)
    except SystemExit as e:
      return e.code


class DatasetsDelete(apitools_base_cli.NewCmd):
  """Command wrapping datasets.Delete."""

  usage = """datasets_delete <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(DatasetsDelete, self).__init__(name, fv)
    flags.DEFINE_boolean(
        'deleteContents',
        None,
        u'If True, delete all the tables in the dataset. If False and the '
        u'dataset contains tables, the request will fail. Default is False',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId):
    """Deletes the dataset specified by the datasetId value. Before you can
    delete a dataset, you must delete all its tables, either manually or by
    specifying deleteContents. Immediately after deletion, you can create
    another dataset with the same name.

    Args:
      projectId: Project ID of the dataset being deleted
      datasetId: Dataset ID of dataset being deleted

    Flags:
      deleteContents: If True, delete all the tables in the dataset. If False
        and the dataset contains tables, the request will fail. Default is
        False
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsDeleteRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    if FLAGS['deleteContents'].present:
      request.deleteContents = FLAGS.deleteContents
    result = client.datasets.Delete(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class DatasetsGet(apitools_base_cli.NewCmd):
  """Command wrapping datasets.Get."""

  usage = """datasets_get <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(DatasetsGet, self).__init__(name, fv)

  def RunWithArgs(self, projectId, datasetId):
    """Returns the dataset specified by datasetID.

    Args:
      projectId: Project ID of the requested dataset
      datasetId: Dataset ID of the requested dataset
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsGetRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    result = client.datasets.Get(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class DatasetsInsert(apitools_base_cli.NewCmd):
  """Command wrapping datasets.Insert."""

  usage = """datasets_insert <projectId>"""

  def __init__(self, name, fv):
    super(DatasetsInsert, self).__init__(name, fv)
    flags.DEFINE_string(
        'dataset',
        None,
        u'A Dataset resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId):
    """Creates a new empty dataset.

    Args:
      projectId: Project ID of the new dataset

    Flags:
      dataset: A Dataset resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsInsertRequest(
        projectId=projectId.decode('utf8'),
        )
    if FLAGS['dataset'].present:
      request.dataset = apitools_base.JsonToMessage(messages.Dataset, FLAGS.dataset)
    result = client.datasets.Insert(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class DatasetsList(apitools_base_cli.NewCmd):
  """Command wrapping datasets.List."""

  usage = """datasets_list <projectId>"""

  def __init__(self, name, fv):
    super(DatasetsList, self).__init__(name, fv)
    flags.DEFINE_boolean(
        'all',
        None,
        u'Whether to list all datasets, including hidden ones',
        flag_values=fv)
    flags.DEFINE_string(
        'filter',
        None,
        u'An expression for filtering the results of the request by label. '
        u'The syntax is "labels.[:]". Multiple filters can be ANDed together '
        u'by connecting with a space. Example: "labels.department:receiving '
        u'labels.active". See https://cloud.google.com/bigquery/docs'
        u'/labeling-datasets#filtering_datasets_using_labels for details.',
        flag_values=fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'The maximum number of results to return',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, to request the next page '
        u'of results',
        flag_values=fv)

  def RunWithArgs(self, projectId):
    """Lists all datasets in the specified project to which you have been
    granted the READER dataset role.

    Args:
      projectId: Project ID of the datasets to be listed

    Flags:
      all: Whether to list all datasets, including hidden ones
      filter: An expression for filtering the results of the request by label.
        The syntax is "labels.[:]". Multiple filters can be ANDed together by
        connecting with a space. Example: "labels.department:receiving
        labels.active". See https://cloud.google.com/bigquery/docs/labeling-
        datasets#filtering_datasets_using_labels for details.
      maxResults: The maximum number of results to return
      pageToken: Page token, returned by a previous call, to request the next
        page of results
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsListRequest(
        projectId=projectId.decode('utf8'),
        )
    if FLAGS['all'].present:
      request.all = FLAGS.all
    if FLAGS['filter'].present:
      request.filter = FLAGS.filter.decode('utf8')
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    result = client.datasets.List(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class DatasetsPatch(apitools_base_cli.NewCmd):
  """Command wrapping datasets.Patch."""

  usage = """datasets_patch <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(DatasetsPatch, self).__init__(name, fv)
    flags.DEFINE_string(
        'dataset',
        None,
        u'A Dataset resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId):
    """Updates information in an existing dataset. The update method replaces
    the entire dataset resource, whereas the patch method only replaces fields
    that are provided in the submitted dataset resource. This method supports
    patch semantics.

    Args:
      projectId: Project ID of the dataset being updated
      datasetId: Dataset ID of the dataset being updated

    Flags:
      dataset: A Dataset resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsPatchRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    if FLAGS['dataset'].present:
      request.dataset = apitools_base.JsonToMessage(messages.Dataset, FLAGS.dataset)
    result = client.datasets.Patch(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class DatasetsUpdate(apitools_base_cli.NewCmd):
  """Command wrapping datasets.Update."""

  usage = """datasets_update <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(DatasetsUpdate, self).__init__(name, fv)
    flags.DEFINE_string(
        'dataset',
        None,
        u'A Dataset resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId):
    """Updates information in an existing dataset. The update method replaces
    the entire dataset resource, whereas the patch method only replaces fields
    that are provided in the submitted dataset resource.

    Args:
      projectId: Project ID of the dataset being updated
      datasetId: Dataset ID of the dataset being updated

    Flags:
      dataset: A Dataset resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryDatasetsUpdateRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    if FLAGS['dataset'].present:
      request.dataset = apitools_base.JsonToMessage(messages.Dataset, FLAGS.dataset)
    result = client.datasets.Update(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class JobsCancel(apitools_base_cli.NewCmd):
  """Command wrapping jobs.Cancel."""

  usage = """jobs_cancel <projectId> <jobId>"""

  def __init__(self, name, fv):
    super(JobsCancel, self).__init__(name, fv)

  def RunWithArgs(self, projectId, jobId):
    """Requests that a job be cancelled. This call will return immediately,
    and the client will need to poll for the job status to see if the cancel
    completed successfully. Cancelled jobs may still incur costs.

    Args:
      projectId: [Required] Project ID of the job to cancel
      jobId: [Required] Job ID of the job to cancel
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsCancelRequest(
        projectId=projectId.decode('utf8'),
        jobId=jobId.decode('utf8'),
        )
    result = client.jobs.Cancel(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class JobsGet(apitools_base_cli.NewCmd):
  """Command wrapping jobs.Get."""

  usage = """jobs_get <projectId> <jobId>"""

  def __init__(self, name, fv):
    super(JobsGet, self).__init__(name, fv)

  def RunWithArgs(self, projectId, jobId):
    """Returns information about a specific job. Job information is available
    for a six month period after creation. Requires that you're the person who
    ran the job, or have the Is Owner project role.

    Args:
      projectId: [Required] Project ID of the requested job
      jobId: [Required] Job ID of the requested job
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsGetRequest(
        projectId=projectId.decode('utf8'),
        jobId=jobId.decode('utf8'),
        )
    result = client.jobs.Get(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class JobsGetQueryResults(apitools_base_cli.NewCmd):
  """Command wrapping jobs.GetQueryResults."""

  usage = """jobs_getQueryResults <projectId> <jobId>"""

  def __init__(self, name, fv):
    super(JobsGetQueryResults, self).__init__(name, fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'Maximum number of results to read',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, to request the next page '
        u'of results',
        flag_values=fv)
    flags.DEFINE_string(
        'startIndex',
        None,
        u'Zero-based index of the starting row',
        flag_values=fv)
    flags.DEFINE_integer(
        'timeoutMs',
        None,
        u'How long to wait for the query to complete, in milliseconds, before'
        u' returning. Default is 10 seconds. If the timeout passes before the'
        u" job completes, the 'jobComplete' field in the response will be "
        u'false',
        flag_values=fv)

  def RunWithArgs(self, projectId, jobId):
    """Retrieves the results of a query job.

    Args:
      projectId: [Required] Project ID of the query job
      jobId: [Required] Job ID of the query job

    Flags:
      maxResults: Maximum number of results to read
      pageToken: Page token, returned by a previous call, to request the next
        page of results
      startIndex: Zero-based index of the starting row
      timeoutMs: How long to wait for the query to complete, in milliseconds,
        before returning. Default is 10 seconds. If the timeout passes before
        the job completes, the 'jobComplete' field in the response will be
        false
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsGetQueryResultsRequest(
        projectId=projectId.decode('utf8'),
        jobId=jobId.decode('utf8'),
        )
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    if FLAGS['startIndex'].present:
      request.startIndex = int(FLAGS.startIndex)
    if FLAGS['timeoutMs'].present:
      request.timeoutMs = FLAGS.timeoutMs
    result = client.jobs.GetQueryResults(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class JobsInsert(apitools_base_cli.NewCmd):
  """Command wrapping jobs.Insert."""

  usage = """jobs_insert <projectId>"""

  def __init__(self, name, fv):
    super(JobsInsert, self).__init__(name, fv)
    flags.DEFINE_string(
        'job',
        None,
        u'A Job resource to be passed as the request body.',
        flag_values=fv)
    flags.DEFINE_string(
        'upload_filename',
        '',
        'Filename to use for upload.',
        flag_values=fv)
    flags.DEFINE_string(
        'upload_mime_type',
        '',
        'MIME type to use for the upload. Only needed if the extension on '
        '--upload_filename does not determine the correct (or any) MIME '
        'type.',
        flag_values=fv)

  def RunWithArgs(self, projectId):
    """Starts a new asynchronous job. Requires the Can View project role.

    Args:
      projectId: Project ID of the project that will be billed for the job

    Flags:
      job: A Job resource to be passed as the request body.
      upload_filename: Filename to use for upload.
      upload_mime_type: MIME type to use for the upload. Only needed if the
        extension on --upload_filename does not determine the correct (or any)
        MIME type.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsInsertRequest(
        projectId=projectId.decode('utf8'),
        )
    if FLAGS['job'].present:
      request.job = apitools_base.JsonToMessage(messages.Job, FLAGS.job)
    upload = None
    if FLAGS.upload_filename:
      upload = apitools_base.Upload.FromFile(
          FLAGS.upload_filename, FLAGS.upload_mime_type,
          progress_callback=apitools_base.UploadProgressPrinter,
          finish_callback=apitools_base.UploadCompletePrinter)
    result = client.jobs.Insert(
        request, global_params=global_params, upload=upload)
    print apitools_base_cli.FormatOutput(result)


class JobsList(apitools_base_cli.NewCmd):
  """Command wrapping jobs.List."""

  usage = """jobs_list <projectId>"""

  def __init__(self, name, fv):
    super(JobsList, self).__init__(name, fv)
    flags.DEFINE_boolean(
        'allUsers',
        None,
        u'Whether to display jobs owned by all users in the project. Default '
        u'false',
        flag_values=fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'Maximum number of results to return',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, to request the next page '
        u'of results',
        flag_values=fv)
    flags.DEFINE_enum(
        'projection',
        u'full',
        [u'full', u'minimal'],
        u'Restrict information returned to a set of selected fields',
        flag_values=fv)
    flags.DEFINE_enum(
        'stateFilter',
        u'done',
        [u'done', u'pending', u'running'],
        u'Filter for job state',
        flag_values=fv)

  def RunWithArgs(self, projectId):
    """Lists all jobs that you started in the specified project. Job
    information is available for a six month period after creation. The job
    list is sorted in reverse chronological order, by job creation time.
    Requires the Can View project role, or the Is Owner project role if you
    set the allUsers property.

    Args:
      projectId: Project ID of the jobs to list

    Flags:
      allUsers: Whether to display jobs owned by all users in the project.
        Default false
      maxResults: Maximum number of results to return
      pageToken: Page token, returned by a previous call, to request the next
        page of results
      projection: Restrict information returned to a set of selected fields
      stateFilter: Filter for job state
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsListRequest(
        projectId=projectId.decode('utf8'),
        )
    if FLAGS['allUsers'].present:
      request.allUsers = FLAGS.allUsers
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    if FLAGS['projection'].present:
      request.projection = messages.BigqueryJobsListRequest.ProjectionValueValuesEnum(FLAGS.projection)
    if FLAGS['stateFilter'].present:
      request.stateFilter = [messages.BigqueryJobsListRequest.StateFilterValueValuesEnum(x) for x in FLAGS.stateFilter]
    result = client.jobs.List(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class JobsQuery(apitools_base_cli.NewCmd):
  """Command wrapping jobs.Query."""

  usage = """jobs_query <projectId>"""

  def __init__(self, name, fv):
    super(JobsQuery, self).__init__(name, fv)
    flags.DEFINE_string(
        'queryRequest',
        None,
        u'A QueryRequest resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId):
    """Runs a BigQuery SQL query synchronously and returns query results if
    the query completes within a specified timeout.

    Args:
      projectId: Project ID of the project billed for the query

    Flags:
      queryRequest: A QueryRequest resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryJobsQueryRequest(
        projectId=projectId.decode('utf8'),
        )
    if FLAGS['queryRequest'].present:
      request.queryRequest = apitools_base.JsonToMessage(messages.QueryRequest, FLAGS.queryRequest)
    result = client.jobs.Query(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class ProjectsList(apitools_base_cli.NewCmd):
  """Command wrapping projects.List."""

  usage = """projects_list"""

  def __init__(self, name, fv):
    super(ProjectsList, self).__init__(name, fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'Maximum number of results to return',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, to request the next page '
        u'of results',
        flag_values=fv)

  def RunWithArgs(self):
    """Lists all projects to which you have been granted any project role.

    Flags:
      maxResults: Maximum number of results to return
      pageToken: Page token, returned by a previous call, to request the next
        page of results
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryProjectsListRequest(
        )
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    result = client.projects.List(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TabledataInsertAll(apitools_base_cli.NewCmd):
  """Command wrapping tabledata.InsertAll."""

  usage = """tabledata_insertAll <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TabledataInsertAll, self).__init__(name, fv)
    flags.DEFINE_string(
        'tableDataInsertAllRequest',
        None,
        u'A TableDataInsertAllRequest resource to be passed as the request '
        u'body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Streams data into BigQuery one record at a time without needing to run
    a load job. Requires the WRITER dataset role.

    Args:
      projectId: Project ID of the destination table.
      datasetId: Dataset ID of the destination table.
      tableId: Table ID of the destination table.

    Flags:
      tableDataInsertAllRequest: A TableDataInsertAllRequest resource to be
        passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTabledataInsertAllRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    if FLAGS['tableDataInsertAllRequest'].present:
      request.tableDataInsertAllRequest = apitools_base.JsonToMessage(messages.TableDataInsertAllRequest, FLAGS.tableDataInsertAllRequest)
    result = client.tabledata.InsertAll(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TabledataList(apitools_base_cli.NewCmd):
  """Command wrapping tabledata.List."""

  usage = """tabledata_list <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TabledataList, self).__init__(name, fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'Maximum number of results to return',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, identifying the result set',
        flag_values=fv)
    flags.DEFINE_string(
        'startIndex',
        None,
        u'Zero-based index of the starting row to read',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Retrieves table data from a specified set of rows. Requires the READER
    dataset role.

    Args:
      projectId: Project ID of the table to read
      datasetId: Dataset ID of the table to read
      tableId: Table ID of the table to read

    Flags:
      maxResults: Maximum number of results to return
      pageToken: Page token, returned by a previous call, identifying the
        result set
      startIndex: Zero-based index of the starting row to read
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTabledataListRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    if FLAGS['startIndex'].present:
      request.startIndex = int(FLAGS.startIndex)
    result = client.tabledata.List(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesDelete(apitools_base_cli.NewCmd):
  """Command wrapping tables.Delete."""

  usage = """tables_delete <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TablesDelete, self).__init__(name, fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Deletes the table specified by tableId from the dataset. If the table
    contains data, all the data will be deleted.

    Args:
      projectId: Project ID of the table to delete
      datasetId: Dataset ID of the table to delete
      tableId: Table ID of the table to delete
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesDeleteRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    result = client.tables.Delete(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesGet(apitools_base_cli.NewCmd):
  """Command wrapping tables.Get."""

  usage = """tables_get <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TablesGet, self).__init__(name, fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Gets the specified table resource by table ID. This method does not
    return the data in the table, it only returns the table resource, which
    describes the structure of this table.

    Args:
      projectId: Project ID of the requested table
      datasetId: Dataset ID of the requested table
      tableId: Table ID of the requested table
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesGetRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    result = client.tables.Get(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesInsert(apitools_base_cli.NewCmd):
  """Command wrapping tables.Insert."""

  usage = """tables_insert <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(TablesInsert, self).__init__(name, fv)
    flags.DEFINE_string(
        'table',
        None,
        u'A Table resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId):
    """Creates a new, empty table in the dataset.

    Args:
      projectId: Project ID of the new table
      datasetId: Dataset ID of the new table

    Flags:
      table: A Table resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesInsertRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    if FLAGS['table'].present:
      request.table = apitools_base.JsonToMessage(messages.Table, FLAGS.table)
    result = client.tables.Insert(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesList(apitools_base_cli.NewCmd):
  """Command wrapping tables.List."""

  usage = """tables_list <projectId> <datasetId>"""

  def __init__(self, name, fv):
    super(TablesList, self).__init__(name, fv)
    flags.DEFINE_integer(
        'maxResults',
        None,
        u'Maximum number of results to return',
        flag_values=fv)
    flags.DEFINE_string(
        'pageToken',
        None,
        u'Page token, returned by a previous call, to request the next page '
        u'of results',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId):
    """Lists all tables in the specified dataset. Requires the READER dataset
    role.

    Args:
      projectId: Project ID of the tables to list
      datasetId: Dataset ID of the tables to list

    Flags:
      maxResults: Maximum number of results to return
      pageToken: Page token, returned by a previous call, to request the next
        page of results
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesListRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        )
    if FLAGS['maxResults'].present:
      request.maxResults = FLAGS.maxResults
    if FLAGS['pageToken'].present:
      request.pageToken = FLAGS.pageToken.decode('utf8')
    result = client.tables.List(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesPatch(apitools_base_cli.NewCmd):
  """Command wrapping tables.Patch."""

  usage = """tables_patch <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TablesPatch, self).__init__(name, fv)
    flags.DEFINE_string(
        'table',
        None,
        u'A Table resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Updates information in an existing table. The update method replaces
    the entire table resource, whereas the patch method only replaces fields
    that are provided in the submitted table resource. This method supports
    patch semantics.

    Args:
      projectId: Project ID of the table to update
      datasetId: Dataset ID of the table to update
      tableId: Table ID of the table to update

    Flags:
      table: A Table resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesPatchRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    if FLAGS['table'].present:
      request.table = apitools_base.JsonToMessage(messages.Table, FLAGS.table)
    result = client.tables.Patch(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


class TablesUpdate(apitools_base_cli.NewCmd):
  """Command wrapping tables.Update."""

  usage = """tables_update <projectId> <datasetId> <tableId>"""

  def __init__(self, name, fv):
    super(TablesUpdate, self).__init__(name, fv)
    flags.DEFINE_string(
        'table',
        None,
        u'A Table resource to be passed as the request body.',
        flag_values=fv)

  def RunWithArgs(self, projectId, datasetId, tableId):
    """Updates information in an existing table. The update method replaces
    the entire table resource, whereas the patch method only replaces fields
    that are provided in the submitted table resource.

    Args:
      projectId: Project ID of the table to update
      datasetId: Dataset ID of the table to update
      tableId: Table ID of the table to update

    Flags:
      table: A Table resource to be passed as the request body.
    """
    client = GetClientFromFlags()
    global_params = GetGlobalParamsFromFlags()
    request = messages.BigqueryTablesUpdateRequest(
        projectId=projectId.decode('utf8'),
        datasetId=datasetId.decode('utf8'),
        tableId=tableId.decode('utf8'),
        )
    if FLAGS['table'].present:
      request.table = apitools_base.JsonToMessage(messages.Table, FLAGS.table)
    result = client.tables.Update(
        request, global_params=global_params)
    print apitools_base_cli.FormatOutput(result)


def main(_):
  appcommands.AddCmd('pyshell', PyShell)
  appcommands.AddCmd('datasets_delete', DatasetsDelete)
  appcommands.AddCmd('datasets_get', DatasetsGet)
  appcommands.AddCmd('datasets_insert', DatasetsInsert)
  appcommands.AddCmd('datasets_list', DatasetsList)
  appcommands.AddCmd('datasets_patch', DatasetsPatch)
  appcommands.AddCmd('datasets_update', DatasetsUpdate)
  appcommands.AddCmd('jobs_cancel', JobsCancel)
  appcommands.AddCmd('jobs_get', JobsGet)
  appcommands.AddCmd('jobs_getQueryResults', JobsGetQueryResults)
  appcommands.AddCmd('jobs_insert', JobsInsert)
  appcommands.AddCmd('jobs_list', JobsList)
  appcommands.AddCmd('jobs_query', JobsQuery)
  appcommands.AddCmd('projects_list', ProjectsList)
  appcommands.AddCmd('tabledata_insertAll', TabledataInsertAll)
  appcommands.AddCmd('tabledata_list', TabledataList)
  appcommands.AddCmd('tables_delete', TablesDelete)
  appcommands.AddCmd('tables_get', TablesGet)
  appcommands.AddCmd('tables_insert', TablesInsert)
  appcommands.AddCmd('tables_list', TablesList)
  appcommands.AddCmd('tables_patch', TablesPatch)
  appcommands.AddCmd('tables_update', TablesUpdate)

  apitools_base_cli.SetupLogger()
  if hasattr(appcommands, 'SetDefaultCommand'):
    appcommands.SetDefaultCommand('pyshell')


run_main = apitools_base_cli.run_main

if __name__ == '__main__':
  appcommands.Run()
