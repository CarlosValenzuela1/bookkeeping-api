from unicodedata import category
from marshmallow import Schema, fields, validate


class InvoiceLinesSchema(Schema):
    '''
    Subschema for the invoice_lines property
    '''
    # invoice_lines = fields.List()
    description = fields.Str(required=True)
    quantity = fields.Integer(required=True, strict=True)
    category = fields.Str(required=True)
    unit_price_net = fields.Str(required=True)


class InvoicePaymentsSchema(Schema):
    '''
    Subschema for the payments property
    '''
    id = fields.Integer(required=True, strict=True)
    amount = fields.Str(required=True)


class JsonSchema(Schema):
    # Main validator schema
    invoice_lines = fields.List(
        fields.Nested(InvoiceLinesSchema),
        required=True,
        validate=validate.Length(min=1)
    )

    payments = fields.List(
        fields.Nested(InvoicePaymentsSchema),
        required=True,
        validate=validate.Length(min=1)
    )
