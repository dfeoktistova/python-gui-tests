def test_delete_group(app):
    old_list = app.groups.get_group_list()
    app.groups.delete_group("New")
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove("New")
    assert sorted(old_list) == sorted(new_list)